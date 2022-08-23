import bs4 as bs4
import requests

class scraper:
    def EscrapearObjetivo(self):
        url = requests.get('https://articulo.mercadolibre.com.ec/MEC-518064367-impresora-multifuncional-epson-ecotank-l3110-local-fisico-_JM?searchVariation=175073686546#searchVariation=175073686546&position=2&search_layout=grid&type=item&tracking_id=e0bde6af-e6b1-450b-93a0-ff509bba469c')
        soup = bs4.BeautifulSoup(url.content, 'html.parser')
        resultEnt = soup.find('span', {'class': 'ui-pdp-buybox__quantity__available'})
        format_result = resultEnt.text.split().__getitem__(0)

        resul = format_result.replace('(', '')
        return resul