from pydantic import BaseModel , Field
from typing import Optional

class Rank(BaseModel):
    overall_rank: Optional[int] = Field(None,description="Overall Happines Rank of the counntry")
class Country(BaseModel):
    country: Optional[str] = Field(None,description="Country Name")
class HappinessScore(BaseModel):
    score: Optional[float] = Field(None,description="Happiness Score of the country")
class GDP(BaseModel):
    gdp_per_capita: Optional[float] = Field(None,description="GDP per capita of the country")
class SocialSupport(BaseModel):
    social_support: Optional[float] = Field(None,description="Social support of the country")
class healthyLifeExpectancy(BaseModel):
    healthy_life_expectancy: Optional[float] = Field(None,description="Healthy life expectancy of the country")
class Freedom(BaseModel):
    freedom_to_make_life_choices: Optional[float] = Field(None,description="Freedom to make life choices of the country")
class Generosity(BaseModel):
    generosity: Optional[float] = Field(None,description="Generosity of the country")
class PerceptionsOfCorruption(BaseModel):
    perceptions_of_corruption: Optional[float] = Field(None,description="Perceptions of corruption of the country")

class CountryRankOnSpecificMetric(BaseModel):
    metric: Optional[str] = Field(None,description="Metric to rank the country by, these are available metrics : score, gdp_per_capita, social_support, healthy_life_expectancy, freedom_to_make_life_choices, generosity, perceptions_of_corruption")
    k: Optional[int] = Field(None,description="Number of countries to return")
    ascending: Optional[bool] = Field(None,description="Ascending or descending order")
