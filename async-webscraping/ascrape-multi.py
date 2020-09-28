from aiohttp import ClientSession
import asyncio
import pathlib

async def fetch(url, session, year):
	async with session.get(url) as resp:
			html_body = await resp.read()
			return {'body':html_body, 'year':year}


async def main(start_year:int= 2020, years_ago:int=5):
	html_body = ''
	tasks= []
	async with ClientSession() as session:
		for i in range(0, years_ago):
			year = start_year - i
			url = f'https://www.boxofficemojo.com/year/{year}/'
			print(f'year : {year} {url}')
			tasks.append(
				asyncio.create_task(
					fetch(url, session, year)
				)
			)
		pages_content = await asyncio.gather(*tasks)
		return pages_content

results = asyncio.run(main())
# print(results)


output_dir = pathlib.Path().resolve() / 'snapshots'
output_dir.mkdir(parents=True, exist_ok=True)

for result in results:
	curr_year = result.get('year')
	html_data = result.get('body')
	output_file = output_dir/f'{curr_year}.html'
	output_file.write_text(html_data.decode())