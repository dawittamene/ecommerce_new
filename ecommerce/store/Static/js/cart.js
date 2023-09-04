var updatBtns = document.getElementsByClassName('update-cart')

for(i=0; i < updatBtns.length; i++){
    updatBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId, 'action:',action)

        console.log('USER:', user)

        if(user === 'AnonymousUser'){
            console.log('user is not login')

        }else{
            console.log('jsdfdsfh')
        }
    })

}