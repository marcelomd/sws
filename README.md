sws
===

"sws" stands for Short Weather Service.

This is a simple script that scrapes weather forecast sites, generates a short digest of the forecast for the next five days and sends it via SMS to a list of recipients. It runs on a simple VPS.

I did it for my in-laws, who live in the countryside. They don't have a reliable internet connection and yet they depend on these forecasts for their farming. This is actually more expensive than 3G internet access for what it offers, but the infrastructure simply isn't there.

We're using [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) for web scraping;
and [Zenvia](http://www.zenvia.com.br/) for the SMS-gateway service.

Currently we look for forecasts for the Ijui - RS region on [Climatempo](http://www.climatempo.com.br/previsao-do-tempo/cidade/1395/ijui-rs) and [Somar Meteorologia](http://somarmeteorologia.com.br/Ijui-RS_Previsao_BR.html).
