# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "http://www.climatempo.com.br/previsao-do-tempo/cidade/1395/ijui-rs"

def digest():
	try:
		html = urlopen(url).read()
		soup = BeautifulSoup(html)

		digest = 'Clima'

		for box in soup.findAll('div', {'class':'box-prev-completa'}):
			# Find forecast date
			txt = box.find('span', {'class':'data-prev'}).text
			r = re.search('(\d+)/\d+', txt)
			date = r.group(1)


			# Max and min temperatures (º == '\xba')
			txt = box.find('span', {'class':'max'}).text
			temp_max = txt.replace('º', '').strip()

			txt = box.find('span', {'class':'min'}).text
			temp_min = txt.replace('º', '').strip()


			# Rain volume
			li = box.find('li', {'class':'prob-chuva-prev-completa'})
			span = li.find('span', {'class':None})
			r = re.search('(\d+)mm', span.text.replace(' ', ''))
			rain = r.group(1)


			# Wind speed
			li = box.find('li', {'class':'velocidade-vento-prev-completa'})
			span = li.find('span', {'class':None})
			r = re.search('(\d+)km/h', span.text.replace(' ', ''))
			wind = r.group(1)


			# Relative humidity
			txt = box.find('span', {'class':'max-relativa'}).text
			rh_max = txt.replace('%', '').strip()

			txt = box.find('span', {'class':'min-relativa'}).text
			rh_min = txt.replace('%', '').strip()
			rh = str(int((int(rh_max) + int(rh_min)) / 2))

			digest += '\n%s: %s-%sC, %smm, %skm, %s%%' % (
					date,
					temp_max, temp_min,
					rain,
					wind,
					rh)

		print('Climatempo(%d chars):' % len(digest))
		print(digest)
		return digest

	except:
		return None


''' MODELO:
...
<p class="clear left paragrafo-padrao">Previsão do tempo atualizada às: 12:40 <span style="font-size: 9px" class="ct-horario-brasilia">(horário de Brasília)</span></p>
...
<div class="box-prev-completa">
	<div class="topo-box">
		<span class="data-prev"> Quarta-Feira, 10/04 </span>
		<div class="por-do-sol"><span class="texto-sol">...</div>
	</div>
	<div class="icones-prev-completa">
		<div class="area-icones-tempo-completa">...</div>
		<ul>
			<li class="maxMin-prev-completa list-style-none">
				<span> Max </span>
				<span class="max">29º</span>
				<span> Min </span>
				<span class="min"> 15º </span>
			</li>
		</ul>
		<ul>
			<li class="prob-chuva-prev-completa list-style-none">
				<span class="left chuva-icone sprite-master"></span>
				<span>5mm<br>80%</span>
			</li>
		</ul>
		<ul>
			<li class="velocidade-vento-prev-completa list-style-none">
				<span class="left vento-icone sprite-master"></span>
				<span>ESE<br>12km/h</span>
			</li>
		</ul>
		<ul>
			<li class="umidade-relativa-prev-completa list-style-none">
				<span class="left ur-icone sprite-master"></span>
				<span class="max-relativa">90%</span>
				<span class="min-relativa">49%</span>
			</li>
		</ul>
	</div>
	<!--...-->
	<div class="clear left subgrid-3 uv">...</div>
	<span class="left left5 paragrafo-padrao top10 fraseologia-prev">...</span>
	<p class="bt-ver-mais-dados left txt-center" id="verdados0">Ver mais dados</p>
	<div id="mostradados0" class="mais-dados">...</div>
</div>
'''
