from fastapi import APIRouter, HTTPException

from app.api.routers.analysis import ANALYSIS_STORE
from app.api.schemas.report import ReportResponse
from app.api.services.export_service import create_report_artifact

router = APIRouter(prefix="/analysis", tags=["reports"])


@router.get("/{analysis_id}/report", response_model=ReportResponse)
def get_report(analysis_id: str) -> ReportResponse:
    if analysis_id not in ANALYSIS_STORE:
        raise HTTPException(status_code=404, detail="analysis not found")

    report = ANALYSIS_STORE[analysis_id]
    report_path = create_report_artifact(
        analysis_id,
        f"Analysis {analysis_id}\n\nMetrics:\n{report.metrics}\n\nInterpretation:\n{report.interpretation}\n",
    )
    return ReportResponse(analysis_id=analysis_id, format="txt", download_url=report_path)
