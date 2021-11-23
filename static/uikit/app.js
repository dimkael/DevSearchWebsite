// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
    hljs.highlightAll();
});

let alert = document.querySelector('.alert');
if (alert) {
    let alertCloseBtn = document.querySelector('.alert__close');
    alertCloseBtn.addEventListener('click', () =>
        alert.style.display = 'none'
    );
}
