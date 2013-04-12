# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "http://somarmeteorologia.com.br/Ijui-RS_Previsao_BR.html"

def digest():
	try:
		html = urlopen(url).read()
		soup = BeautifulSoup(html)

		digest = 'Somar'

		# Do only for 5 days
		for box in soup.body.findAll('table', {'width':'100%', 'bgcolor':'#FBFBFB'})[:5]:
			# Forecast date
			txt = box.find('td', {'width':'39%'}).text
			r = re.search('(\d+) de', txt)
			date = r.group(1)


			# Max and min temperatures
			txt = box.find('div', {'class':'prevmax'}).text
			temp_max = txt.replace('°C', '').strip()

			txt = box.find('div', {'class':'prevmin'}).text
			temp_min = txt.replace('°C', '').strip()


			# Rain volume
			txt = box.find('td', text=re.compile('\d+\s*mm')).text
			rain = txt.replace('m', '').strip()


			# Wind speed
			txt = box.find('td', text=re.compile('\d+\s*km/h')).text
			wind = txt.replace('km/h', '').strip()


			# Relative humidity
			txt = box.find('td', text=re.compile('\d+\s*%')).text
			rh = txt.replace('%', '').strip()


			digest += '\n%s: %s-%sC, %smm, %skm, %s%%' % (
					date,
					temp_max, temp_min,
					rain,
					wind,
					rh)

		print('Somar(%d chars):' % len(digest))
		print(digest)
		return digest

	except:
		return None


''' MODEL:
...
<p><strong>Atualizado em:</strong> 11/04/2013 - 04:02:03</p>
...
<table width="100%" bgcolor="#FBFBFB" border="1px" bordercolor="#F4F4F4">
	<tbody>
		<tr>
			<td colspan="7">
				<table width="100%" style="border-collapse:collapse">
					<tbody>
						<tr>
							<td width="39%" style="padding-top:8px;"><div class="texto_tbl_titulo">Quinta-feira, 11 de Abril</div></td>
							<td width="29%" style="padding-top:8px;"><div class="texto_tbl_titulo" align="right">Nascer e Pôr-do-Sol</div></td>
							<td width="17%" style="padding-top:8px;"><div class="texto_tbl_titulo" align="center"><img src="http://img01.somarmeteorologia.com.br/icones/sol_nasc.gif"> 06h58m</div></td>
							<td width="15%" style="padding-top:8px;"><div class="texto_tbl_titulo" align="center"><img src="http://img02.somarmeteorologia.com.br/icones/sol_por.gif"> 18h10m</div></td>
						</tr>
					</tbody>
				</table>
			</td>
		</tr>
		<tr>
			<td align="center">
				<table style="border-collapse:collapse;">
					<tbody>
						<tr>
							<td align="center"><div class="icone-p ppn-md"></div></td>
						</tr>
						<tr>
							<td align="center">madrug.</td>
						</tr>
					</tbody>
				</table>
			</td>
			<td align="center">
				<table style="border-collapse:collapse;">
					<tbody>
						<tr>
							<td align="center"><div class="icone-p pnb"></div></td>
						</tr>
						<tr>
							<td align="center">manhã</td>
						</tr>
					</tbody>
				</table>
			</td>
			<td align="center">
				<table style="border-collapse:collapse;">
					<tbody>
						<tr>
							<td align="center"><div class="icone-p ppc-t"></div></td>
						</tr>
						<tr>
							<td align="center">tarde</td>
						</tr>
					</tbody>
				</table>
			</td>
			<td align="center">
				<table style="border-collapse:collapse;">
					<tbody>
						<tr>
							<td align="center"><div class="icone-p ppc-n"></div></td>
						</tr>
						<tr>
							<td align="center">noite</td>
						</tr>
					</tbody>
				</table>
			</td>
			<td align="center">
				<table style="border-collapse:collapse">
					<tbody>
						<tr>
							<td align="center"><img src="http://img03.somarmeteorologia.com.br/icones/ic_temp_up.gif" alt="temperatura maxima" title="temperatura maxima"></td>
							<td> <div class="prevmax">25 °C</div></td>
						</tr>
						<tr>
							<td align="center"><img src="http://img03.somarmeteorologia.com.br/icones/ic_temp_down.gif" alt="temperatura minima" title="temperatura minima"></td>
							<td> <div class="prevmin">17 °C</div></td>
						</tr>
					</tbody>
				</table>
			</td>
			<td align="center">
				<table style="border-collapse:collapse">
					<tbody>
						<tr>
							<td align="center"><img src="http://img01.somarmeteorologia.com.br/icones/icone_chuva.gif" alt="precipitação" title="precipitação"></td>
							<td align="center">6  mm</td>
						</tr>
						<tr>
							<td align="center"><img src="http://img02.somarmeteorologia.com.br/icones/icone_umidade.gif" alt="umidade" title="umidade"></td>
							<td align="center">75%</td>
						</tr>
					</tbody>
				</table>
			</td>
			<td align="center">
				<table style="border-collapse:collapse">
					<tbody>
						<tr>
							<td align="center"><img src="http://img03.somarmeteorologia.com.br/icones/vento_dir.gif" alt="direção do vento" title="direção do vento"></td>
							<td align="center">NNE</td>
						</tr>
						<tr>
							<td align="center"><img src="http://img01.somarmeteorologia.com.br/icones/vento_vel.gif" alt="velocidade do vento" title="velocidade do vento"></td>
							<td align="center">14km/h</td>
						</tr>
					</tbody>
				</table>
			</td>
		</tr>
		<tr>
			<td colspan="7" style="padding-left:10px;">Sol, alternando com pancadas de chuva e possíveis trovoadas</td>
		</tr>
	</tbody>
</table>


'''
