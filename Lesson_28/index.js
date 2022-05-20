'use strict'

let inp = document.querySelector('input')
let btn = document.querySelector('button')
let h1 = document.querySelector('h1')

let obj = {
    name: 'Abzi',
    age: 18,
    married: false
}
let object = JSON.parse(localStorage.getItem('flex'))
h1.innerHTML = object.age


btn.addEventListener('click', () => {
    // JSON.stringify(localStorage.setItem('text', obj));
    localStorage.setItem('flex', JSON.stringify(obj))
    // localStorage.setItem('text', obj.age)
    h1.innerHTML = inp.value
    inp.value = ''
})
