function deleteAsteriskFields(){
    document.querySelectorAll('.asteriskField').forEach((item)=>{
        item.remove()
    })
}
function leftSmallUl(){
    document.getElementById('hint_id_password1').querySelector('ul').style.paddingLeft = '0';
}