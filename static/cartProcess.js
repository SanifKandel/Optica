let cartUpdate = document.getElementsByClassName('addToCart');
for(let i=0; i < cartUpdate.length; i++){
    cartUpdate[i].addEventListener('click',function(){
        let product = this.dataset.product;
        let action = this.dataset.action;
        console.log(product)
        console.log(action)
        let url = '/addCart/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' :  csrftoken,
        },
        body:JSON.stringify({'product': product, 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
    })

    }

