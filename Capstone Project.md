eir# Introduction/Business Problem
The COVID-19 pandemic has taken an unprecedented toll globally, already affecting over 2M people, taking over 200K lives and, according to WEF, will likely cost the world 2 trillion USD in economic losses.

In the Philippines, the responsibility of managing the quarantine falls on the shoulders of the mayors of the cities and municipalities.

Not all cities are affected by the virus the same way. Some cities are overwhelmed by the number of cases. Some cities have seen the peak and are now slowly coming down in terms of cases. Some cities are growing in terms of the number of cases.

The mayors will be interested to see where their city is relative to cases. Is their city on the downward path or in the growth path?

The citizens, on the other hand, will be interested to know where the hospitals are near their location.

This is the problem we want to solve with data analysis.

As an application, we would have an interface for mayors to see if their daily rates of cases are growing or decreasing.

For citizens, they can find out the nearest health facilities and testing centers are so they can go there in case they need to be tested or see a healthcare professional.

# Data Section
For this exercise, we will be using the following datasets:

1. Case Information dataset provided by the Philippine Department of Health. We will use this dataset to determine the growth rates per city. This dataset includes the following fields:
	* CaseCode : Random code assigned for labelling cases
	* Age : Age
	* AgeGroup : Five-year age group
	* Sex : Sex
	* DateRepConf : Date publicly announced as confirmed case
	* DateRecover : Date recovered
	* DateDied : Date died
	* RemovalType : Type of removal (recovery or death)
	* DateRepRem : Date publicly announced as removed
	* Admitted : Binary variable indicating patient has been admitted to hospital
	* RegionRes : Region of residence
	* ProvCityRes : Province of residence
	* RegionPSGC : Philippine Standard Geographic Code of Region of Residence
	* ProvPSGC : Philippine Standard Geographic Code of Province of Residence
	* MunCityPSGC : Philippine Standard Geographic Code of Municipality or City of Residence
	* HealthStatus : Known current health status of patient (asymptomatic, mild, severe, critical, died, recovered)
	* Quarantined : Ever been home quarantined, not necessarily currently in home quarantine
2. Geojson dataset of cities and municipalities in the Philippines. We will use this dataset to provide the mapping boundaries of the different cities and municipalities in the Philippines.
	* ID_0 : Unique ID 0
	* ISO : ISO Country Code
	* NAME_0 : Country Name
	* NAME_2 : Municipality or City Name
	* PROVINCE : Province Name
	* REGION : Regiona Name
	* geometry : Polygon, coordinates
3. Foursquare Search API. We will use this dataset to provide us with with information of health related venues especially their location expressed in latitudes and longitudes. We will also use the categories as a filter. We will bash this data with the boundaries provided by the city geojson dataset above. The Foursquare Search API returns the following data:
	* id : A unique string identifier for this venue.
	* name : The best known name for this venue.
	* location : An object containing none, some, or all of address (street address), crossStreet, city, state, postalCode, country, lat, lng, and distance. All fields are strings, except for lat, lng, and distance. Distance is measured in meters. Some venues have their locations intentionally hidden for privacy reasons (such as private residences). If this is the case, the parameter isFuzzed will be set to true, and the lat/lng parameters will have reduced precision.
	* categories : An array, possibly empty, of categories that have been applied to this venue. One of the categories will have a primary field indicating that it is the primary category for the venue. For the complete category tree, see categories.
