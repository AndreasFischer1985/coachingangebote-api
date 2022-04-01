# coachingangebote.DefaultApi

All URIs are relative to *https://rest.arbeitsagentur.de/infosysbub/avgs*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aktivierungsangebote**](DefaultApi.md#aktivierungsangebote) | **GET** /pc/v1/aktivierungsangebote | Coaching-/Aktivierungsangebote


# **aktivierungsangebote**
> Response aktivierungsangebote(mz)

Coaching-/Aktivierungsangebote

Die Suche nach Coaching-/Aktivierungsangeboten ermöglicht verfügbare Weiterbildungsangebote mit verschiedenen GET-Parametern zu filtern.

### Example

* OAuth Authentication (clientCredAuth):

```python
import time
from deutschland import coachingangebote
from deutschland.coachingangebote.api import default_api
from deutschland.coachingangebote.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to https://rest.arbeitsagentur.de/infosysbub/avgs
# See configuration.py for a list of all supported configuration parameters.
configuration = coachingangebote.Configuration(
    host = "https://rest.arbeitsagentur.de/infosysbub/avgs"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: clientCredAuth
configuration = coachingangebote.Configuration(
    host = "https://rest.arbeitsagentur.de/infosysbub/avgs"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with coachingangebote.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    mz = "SA%2001" # str | Maßnahmenziel - SA%2001 = Heranführung an den Ausbildungs- und Arbeitsmarkt sowie Feststellung, Verringerung und Beseitigung von Vermittlungshemmnissen; SA%2004 = Heranführung an eine selbständige Arbeit; SA%2005 = Stabilisierung einer Beschäftigungsaufnahme.
    sw = "Vermittlungshemmnisse" # str | Suchwort (optional)
    ort = "Feucht_90537_11.224918_49.376701" # str | Ortsangabe nebst Postleitzahl und Koordinaten (optional)
    pg = 1 # int | Ergebnissseite (beginnend mit 0) (optional)
    re = "BY" # str | Region/Bundesland - BW=Baden-Württemberg; BY=Bayern; BE=Berlin; BB=Brandenburg; HB=Bremen; HH=Hamburg; HE=Hessen; MV=Mecklenburg-Vorpommern; NI=Niedersachsen; NW=Nordrhei-Westfalen; RP=Rheinland-Pfalz; SL=Saarland; SN=Sachsen; ST=Sachsen-Anhalt; SH=Schleswig-Holstein; TH=Thüringen. Mehrere Komma-getrennte Angaben möglich. (optional)
    ban = 229563 # int | Anbieter-ID (optional)
    uk = "Bundesweit" # str | Umkreis - Bundesweit=Bundesweit; 25=25 km; 50=50 km; 100=100 km; 150=150 km; 200=200 km. (optional)
    mna = 0 # int | Maßnahmenart - 0=Einzelmaßnahme; 1=Gruppenmaßnahme. Komma-separierte Angaben möglich. (optional)
    deufoev = True # bool | DEUFOEV - true = (nur) Anbieter berufsbezogener Sprachförderung Deutsch (DeuFöV) anzeigen. (optional)
    sort = "ta" # str | Sortierungskriterium - ta = Maßnahmetitel A-Z; tz = Maßnahmetitel Z-A. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Coaching-/Aktivierungsangebote
        api_response = api_instance.aktivierungsangebote(mz)
        pprint(api_response)
    except coachingangebote.ApiException as e:
        print("Exception when calling DefaultApi->aktivierungsangebote: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Coaching-/Aktivierungsangebote
        api_response = api_instance.aktivierungsangebote(mz, sw=sw, ort=ort, pg=pg, re=re, ban=ban, uk=uk, mna=mna, deufoev=deufoev, sort=sort)
        pprint(api_response)
    except coachingangebote.ApiException as e:
        print("Exception when calling DefaultApi->aktivierungsangebote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mz** | **str**| Maßnahmenziel - SA%2001 &#x3D; Heranführung an den Ausbildungs- und Arbeitsmarkt sowie Feststellung, Verringerung und Beseitigung von Vermittlungshemmnissen; SA%2004 &#x3D; Heranführung an eine selbständige Arbeit; SA%2005 &#x3D; Stabilisierung einer Beschäftigungsaufnahme. |
 **sw** | **str**| Suchwort | [optional]
 **ort** | **str**| Ortsangabe nebst Postleitzahl und Koordinaten | [optional]
 **pg** | **int**| Ergebnissseite (beginnend mit 0) | [optional]
 **re** | **str**| Region/Bundesland - BW&#x3D;Baden-Württemberg; BY&#x3D;Bayern; BE&#x3D;Berlin; BB&#x3D;Brandenburg; HB&#x3D;Bremen; HH&#x3D;Hamburg; HE&#x3D;Hessen; MV&#x3D;Mecklenburg-Vorpommern; NI&#x3D;Niedersachsen; NW&#x3D;Nordrhei-Westfalen; RP&#x3D;Rheinland-Pfalz; SL&#x3D;Saarland; SN&#x3D;Sachsen; ST&#x3D;Sachsen-Anhalt; SH&#x3D;Schleswig-Holstein; TH&#x3D;Thüringen. Mehrere Komma-getrennte Angaben möglich. | [optional]
 **ban** | **int**| Anbieter-ID | [optional]
 **uk** | **str**| Umkreis - Bundesweit&#x3D;Bundesweit; 25&#x3D;25 km; 50&#x3D;50 km; 100&#x3D;100 km; 150&#x3D;150 km; 200&#x3D;200 km. | [optional]
 **mna** | **int**| Maßnahmenart - 0&#x3D;Einzelmaßnahme; 1&#x3D;Gruppenmaßnahme. Komma-separierte Angaben möglich. | [optional]
 **deufoev** | **bool**| DEUFOEV - true &#x3D; (nur) Anbieter berufsbezogener Sprachförderung Deutsch (DeuFöV) anzeigen. | [optional]
 **sort** | **str**| Sortierungskriterium - ta &#x3D; Maßnahmetitel A-Z; tz &#x3D; Maßnahmetitel Z-A. | [optional]

### Return type

[**Response**](Response.md)

### Authorization

[clientCredAuth](../README.md#clientCredAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

