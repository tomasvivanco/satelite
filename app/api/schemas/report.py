from pydantic import BaseModel


class ReportResponse(BaseModel):
    analysis_id: str
    format: str
    download_url: str
