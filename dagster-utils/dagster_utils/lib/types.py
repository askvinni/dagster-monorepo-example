from typing import Optional

import pandas as pd
from dagster import usable_as_dagster_type
from pydantic import BaseModel


@usable_as_dagster_type
class UtilsFileSystemOutputType(BaseModel):
    """Represents a file in the file system. Includes the properties `filename`,
    `extension`, and `content`, representing the encoded content."""

    filename: str
    content: bytes
    meta: Optional[dict]

    @property
    def extension(self):
        return self.filename.split(".")[-1].lower()


@usable_as_dagster_type
class UtilsSinkInputType(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    """Represents the type that should be used to load data into a utils-defined sink."""

    dest_asset: str
    data: pd.DataFrame
    meta: Optional[dict]
