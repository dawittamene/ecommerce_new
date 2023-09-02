var updatBtns = document.getElementsByClassName('update-cart')

for(i=0; i < updatBtns.length; i++){
    updatBtns[i].addEventListener('click', function(){
        var productID = this.dataset.product
        var action = this.dataset.action
        console.log('productID:',productID, 'action:',action)

        console.log('USER:', user)

        if(user === 'AnonymousUser'){
            console.log('user is not login')

        }else{
            updateUserOrder(productID, action)
        }
    })

}

function updateUserOrder(productID, action){
    console.log('user is logged in, sending data....')
    var url = '/update_item/'

    fatch(url,{
        method:'POST',
        headers:{
            'content-Type':'application/json',
            'X-CSRFTOKEN':csrftoken,
        },
        body:JSON.stringify({'productID': productID, 'action':action})
    })
    .then((response) =>{
        return response.json
    })

    .then((data) =>{
        console.log('data:', data)
    })
}