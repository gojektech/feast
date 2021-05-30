import os
import pathlib
import shutil
import stat
import subprocess
import textwrap
from distutils.dir_util import copy_tree

import yaml
from jinja2 import Template


def get_repo_root():
    return pathlib.Path(
        (
            subprocess.Popen(
                ["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE
            )
            .communicate()[0]
            .rstrip()
            .decode("utf-8")
        )
    )


reserved_tags = [
    "code",
    "endcode",
]


def get_code_block_function(config, source_dir: pathlib.Path):
    def get_code_block(name):
        for step in config["steps"]:
            if step["name"] == name:
                if "command" in step:
                    language = "bash"
                    code = textwrap.dedent(step["command"])
                elif "python_script" in step:
                    language = "python"
                    with open(source_dir / step["python_script"]) as f:
                        snippet = f.read()
                        code = textwrap.dedent(snippet)
                else:
                    raise ValueError(
                        "Must provide either command or python_script as part of config.yml steps."
                    )

                block = (
                    "{% code %}\n"
                    f"```{language}\n"
                    f"{code}"
                    "\n```"
                    "\n{% endcode %}"
                )
                return block

        raise Exception(f"Could not find step in the script named {name}")

    return get_code_block


def find_reserved_tag_start(row, from_char):
    for tag in reserved_tags:
        start = row.find(f"{from_char}% {tag} ")
        if start > -1:
            return start
    return -1


def normalize_gitbook_tags(
    doc_template_str, from_open, from_closed, to_open, to_closed
):
    result = []
    for row in doc_template_str:
        start = find_reserved_tag_start(row, from_open)
        if start >= 0:
            end = row.find(f"%{from_closed}", start)
            chars = list(row)
            chars[start] = to_open
            chars[end + 1] = to_closed
            result += ["".join(chars)]
        else:
            result += [row]
    return result


def render_template(source_dir: pathlib.Path):
    """
    Renders documentation and a test script for specific folder

    Each folder must contain a config.yml containing code snippets

    Args:
        source_dir: Folder containing config.yml
    """
    with open(source_dir / "config.yml") as file:
        config = yaml.safe_load(file)

    with open(get_repo_root() / "docgen/test_script.jinja2") as file:
        test_template_contents = file.read()

    build_dir = source_dir / "build"

    # Set up build directory fo
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    test_script_path = build_dir / "test_script.sh"

    # generate the test script
    test_template = Template(test_template_contents.strip())
    rendered_test_script = test_template.render(config)

    # write the test script
    with open(test_script_path, "w") as f:
        f.write(rendered_test_script)

    # Make test script executable
    st = os.stat(test_script_path)
    os.chmod(test_script_path, st.st_mode | stat.S_IEXEC)

    # Copy test files to build dir
    for step in config["steps"]:
        if "python_script" in step:
            shutil.copy(source_dir / step["python_script"], build_dir)

    # Add lookup function to fetch code blocks
    config["get_code_block"] = get_code_block_function(config, source_dir)

    # Load documentation template
    template_path = source_dir / "document.jinja2"

    # Render documentation template
    with open(template_path) as f:
        doc_template_rows = f.readlines()
        # We need to remove conflicting characters between jinja and gitbook
        doc_template_rows = normalize_gitbook_tags(
            doc_template_rows, "{", "}", "[", "]"
        )

        # Generate documentation
        doc_template = Template("".join(doc_template_rows).strip())
        rendered_doc_unnormalized = doc_template.render(config)

        # Add back conflicting characters after template rendering is done
        rendered_doc = "\n".join(
            normalize_gitbook_tags(
                rendered_doc_unnormalized.split("\n"), "[", "]", "{", "}"
            )
        )
        staged_documentation_path = build_dir / "document.md"
        with open(staged_documentation_path, "w") as f_doc:
            f_doc.write(rendered_doc)

    # Update Gitbook documentation using rendered document
    shutil.copy(
        build_dir / "document.md", get_repo_root() / config["gitbook_output_file"]
    )

    # Copy test scripts to Python SDK tests folder
    from_dir = str(build_dir.absolute())
    to_dir = str(get_repo_root() / "sdk/python/tests/doctests" / source_directory.name)
    copy_tree(from_dir, to_dir)

    # Remove unnecessary document.md in tests folder
    document_path = os.path.join(to_dir, "document.md")
    if os.path.exists(document_path):
        os.remove(document_path)

    print(f"Rendered documentation template for {source_dir.name}")

    return source_dir, test_script_path, staged_documentation_path


if __name__ == "__main__":
    docgen_dir = get_repo_root() / "docgen"
    for source_directory in [f for f in docgen_dir.iterdir() if f.is_dir()]:
        render_template(source_directory)
