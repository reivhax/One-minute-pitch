$('document').ready(()=>{
  delete=(comment)=>{
    $.ajax({
      url:'/delete/'+comment,
      method:'POST',
      success:(data)=>{
        if (data=='Success'){
          l=$('#pitch'+pitch)[0].textContent
          dislikes=parseInt(l)
          dislikes++
          $('#dislike'+pitch)[0].textContent=' '+dislikes.toString()+' '
        }
      }
    })
  }
})
