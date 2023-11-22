from langchain.tools.base import BaseTool
from typing import Type
from pydantic import BaseModel
from tool_inputs import *
from functions import *
from base_inputs import Continent
class RankCountriesTool(BaseTool):
    name = "RankCountries"
    description = "Rank countries by a specific metric"
    args_schema : Type[BaseModel] = CountryRankOnSpecificMetric
    return_direct  = True

    def _run(self,**kwargs):
        response = rank_countries_by_metric(**kwargs)
        return response
    
class PlotScatterTool(BaseTool):
    name = "PlotScatterPlot"
    description = "Plot scatter plot for countries compraing 2 different countries"
    args_schema : Type[BaseModel] = PlotScatterPlot
    return_direct  = True

    def _run(self,**kwargs):
        response = plot_scatter(**kwargs)
        return response

class PlotPairPlotTool(BaseTool):
    name="PlotPairPlot"
    description = "Plot pair plot for countries"
    return_direct=True
    args_schema: Type[BaseModel] = Continent
    def _run(self,**kwargs):
        response = create_pair_plot(**kwargs)
        return response
class PlotContinentTool(BaseTool):
    name="ContinentPlot"
    description = "plot for continents"
    return_direct=True
    args_schema: Type[BaseModel] = ContinentPlot
    def _run(self,**kwargs):
        response = create_continent_plot(**kwargs)
        return response