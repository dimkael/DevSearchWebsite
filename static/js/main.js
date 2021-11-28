let searchFrom = document.querySelector('.search-form')
let pageLinks = document.querySelectorAll('.page-link')

if (searchFrom) {
    for (let i = 0; i < pageLinks.length; i++) {
        pageLinks[i].addEventListener('click', function(e) {
            e.preventDefault()

            let page = this.dataset.page

            searchFrom.innerHTML += `<input value=${page} name="page" hidden>`
            searchFrom.submit()
        })
    }
}