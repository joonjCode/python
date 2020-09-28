from aiohttp import ClientSession
import asyncio
import pathlib


async def main():
	url = 'https://www.boxofficemojo.com/year/2019/'
	async with ClientSession() as session:
		async with session.get(url) as resp:
			html_body = await resp.read()
			return html_body


html_data = asyncio.run(main())
output_dir = pathlib.Path().resolve() / 'snapshots'
output_dir.mkdir(parents=True, exist_ok=True)
output_file =output_dir/'2019.html'
output_file.write_text(html_data.decode())


