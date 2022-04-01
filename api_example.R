#----------------
# Simple Example
#----------------
install.packages(c("devtools","rjson","httr"))
devtools::install_github("AndreasFischer1985/qqBaseX")
clientId="ee971dcb-96fa-47b3-b2be-00863e4fc88b"
clientSecret="1050e0b7-6db8-49e8-aff9-0e58e556681f"
postData=list( "grant_type"="client_credentials","client_id"=clientId,"client_secret"=clientSecret) 
token_request=httr::POST(
        url="https://rest.arbeitsagentur.de/oauth/gettoken_cc",
        body=postData,encode="form",
        config=httr::config(connecttimeout=60))
token=httr::content(token_request, as='parsed')$access_token
url="https://rest.arbeitsagentur.de/infosysbub/avgs/pc/v1/aktivierungsangebote?mz=SA%2001&uk=Bundesweit&deufoev=false&page=1"
data_request=httr::GET(url=url, httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        config=httr::config(connecttimeout=60))
data_request
data=rawToChar(httr::content(data_request))

