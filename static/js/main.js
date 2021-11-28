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

let formFields = document.querySelectorAll('.form__field')
if (formFields) {
    for (let i = 0; i < formFields.length; i++) {
        let input = formFields[i].children[1]
        input.setAttribute('class', 'input input--text')
        input.setAttribute('placeholder', 'Add text')
    }
}