from langchain.tools.base import BaseTool
from typing import Type
from pydantic import BaseModel
from ToolInputs import *
from functions import rank_countries_by_metric
class RankCountriesTool(BaseTool):
    name = "RankCountries"
    description = "Rank countries by a specific metric"
    args_schema : Type[BaseModel] = CountryRankOnSpecificMetric

    def _run(self,**kwargs):
        response = rank_countries_by_metric(**kwargs)
        return response