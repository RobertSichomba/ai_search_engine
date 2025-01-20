from django.shortcuts import render
from .models import ScrapedData
from .scraper import scrape_url

def search(request):
    query = request.GET.get('q')  # Get the search query
    results = []  # Initialize results as an empty list

    if query:
        print(f"Search Query: {query}")  # Debugging: Print the query
        if query.startswith('http://') or query.startswith('https://'):
            # Scrape the URL
            scraped_data = scrape_url(query)
            if scraped_data:
                # Save scraped data to the database
                ScrapedData.objects.create(
                    url=query,
                    title=scraped_data['title'],
                    content=scraped_data['content']
                )
                results = ScrapedData.objects.filter(url=query)
        else:
            # Perform a keyword search
            results = ScrapedData.objects.filter(content__icontains=query)
        print(f"Results: {results}")  # Debugging: Print the results

    return render(request, 'search/search.html', {'results': results, 'query': query})