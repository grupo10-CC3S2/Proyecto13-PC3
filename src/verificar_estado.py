import os
import json
import sys


def check_tfstate_files():
    results = {"modules": {}, "total_resources": 0, "status": "ok"}

    tfstate_paths = []

    monorepo_path = "../iac/monorepo"
    if os.path.exists(monorepo_path):
        for root, dirs, files in os.walk(monorepo_path):
            for file in files:
                if file.endswith(".tfstate"):
                    tfstate_paths.append(os.path.join(root, file))

    multirepo_path = "../iac/multirepo/umbrella-repo"
    if os.path.exists(multirepo_path):
        for root, dirs, files in os.walk(multirepo_path):
            for file in files:
                if file.endswith(".tfstate"):
                    tfstate_paths.append(os.path.join(root, file))

    # Analizar cada archivo
    for tfstate_path in tfstate_paths:
        module_name = os.path.basename(os.path.dirname(tfstate_path))

        try:
            with open(tfstate_path, "r") as f:
                state_data = json.load(f)

            resource_count = len(state_data.get("resources", []))
            results["modules"][module_name] = {
                "path": tfstate_path,
                "resources": resource_count,
                "terraform_version": state_data.get("terraform_version",
                                                    "unknown"),
            }
            results["total_resources"] += resource_count

        except Exception as e:
            results["modules"][module_name] = {"path": tfstate_path, "error":
                                               str(e)}
            results["status"] = "error"

    return results


def generate_report(output_file=None):
    results = check_tfstate_files()

    output_file = "report.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Reporte guardado: {output_file}")

    return 0 if results["status"] == "ok" else 1


if __name__ == "__main__":
    exit_code = generate_report()
    sys.exit(exit_code)
