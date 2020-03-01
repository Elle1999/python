from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def parse_search_results(search_page_url):
    job_links = []
    headers = {'User-Agent':'Mozilla/5.0'}

    #Get raw HTML, format as BS4 object
    search_results = requests.get(search_page_url, headers)
    soup = BeautifulSoup(search_results.text, 'html.parser')

    #Find all divs containing job postings
    job_listings = soup.find_all("div", class_="jobsearch-SerpJobCard")

    #Parse divs for job links
    for listing in job_listings:
        link = "https://www.indeed.com" + listing.find("a", class_="jobtitle").attrs['href']
        job_links.append(link)

    return job_links

def find_jobs(job_title, city, state_code, amount=100):
    base_url = "https://www.indeed.com/jobs?q={job}&l={location}%2C+{state}"
    job_links = []

    #Replace spaces with "+" for URL formatting
    job = "+".join(job_title.split())
    location = "+".join(city.split())

    base_search_page_url = base_url.format(job=job, location=location, state=state_code)

    #Find and parse search result pages
    for i in range(amount//10):
        search_page_url = base_search_page_url + '&start={}'.format(i*10)
        job_links.extend(parse_search_results(search_page_url))

    return set(job_links)


def run_search():
    job_title = entry_job_title.get()
    city = entry_city.get()
    state_code = entry_state_code.get()

    jobs = find_jobs(job_title, city, state_code, amount=200)

    for job in jobs:
        listbox.insert(END, job)

main = Tk()
main.title("Jobspyder")
main.geometry('1920x1080')
main.config(bg = '#fffcf2')

label_job_title = Label(main, text = 'Job Title:')
label_job_title.grid(row = 0, column = 0, padx = 20, pady = 10)

entry_job_title = Entry(main, width = 20)
entry_job_title.grid(row = 0, column = 1)

label_city = Label(main, text='City:')
label_city.grid(row = 1, column = 0, padx = 20, pady = 10)

entry_city = Entry(main, width = 20)
entry_city.grid(row = 1, column = 1)

label_state_code = Label(main, text = 'State Code:')
label_state_code.grid(row = 2, column = 0, padx = 20, pady = 10)

entry_state_code = Entry(main, width = 20)
entry_state_code.grid(row = 2, column = 1)

listbox = Listbox(main, height=100, width=300)
listbox.grid(row = 4, column = 5)

btn = Button(main, text='Search', command = run_search)
btn.grid(row = 3, column = 1)




main.mainloop()