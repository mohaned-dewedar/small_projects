from pydantic import BaseModel , Field
from typing import Optional
available_metrics = "score, gdp_per_capita, social_support, healthy_life_expectancy, freedom_to_make_life_choices, generosity, perceptions_of_corruption"


class Metrics(BaseModel):
    metric: str= Field(...,description=f"Metric to rank the country by, these are available metrics : {available_metrics}")
    

class CountryRankOnSpecificMetric(Metrics):
    k: Optional[int] = Field(None,description="Number of countries to return")
    ascending: Optional[bool] = Field(None,description="Ascending or descending order")

class PlotScatterPlot(BaseModel):
    continent : Optional[str] = Field(None,description="Continent to filter by")
    metric_x : str= Field(...,description=f"Metric to plot on the x axis, these are available metrics : {available_metrics}")
    metric_y : str = Field(...,description=f"Metric to plot on the y axis, these are available metrics : {available_metrics}")

class ContinentPlot(Metrics):
    chart_type: Optional[str] = Field('bar',description="Type of chart to plot these are available options box','bar', or 'histogram'")