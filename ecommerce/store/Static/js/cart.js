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
            console.log('user is authenticated, sending data....')
        }
    })

}