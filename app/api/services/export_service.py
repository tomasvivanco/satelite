from pathlib import Path


def create_report_artifact(analysis_id: str, content: str) -> str:
    output_dir = Path("artifacts/reports")
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / f"{analysis_id}.txt"
    report_path.write_text(content, encoding="utf-8")
    return str(report_path)
