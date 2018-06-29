$('document').ready(()=>{
  $('#createform').submit((event)=>{
    event.preventDefault()
    pitch=$('#Pitch').val().trim()
    if (pitch.length < 2){return}
    $.ajax(
      {
        url:'/newpitch',
        method:'GET',
        data:{
          'pitch':pitch
        },
        success:(data)=>{
          $('#pitches').empty()
          $('#pitches').append(data)
        },
        error: (data)=>{
          alert('Could not post pitch')
        }
      }
    )
  })
  like=(pitch)=>{
    $.ajax(
      {
        url:'/like/'+pitch,
        method:'GET',
        success:(data)=>{
          if (data=='Success'){
            l=$('#like'+pitch)[0].textContent
            likes=parseInt(l)
            likes++
            $('#like'+pitch)[0].textContent=' '+likes.toString()+' '
          }
        }
      }
    )
  }
  like=(pitch)=>{
    $.ajax(
      {
        url:'/like/'+pitch,
        method:'GET',
        success:(data)=>{
          if (data=='Success'){
            l=$('#like'+pitch)[0].textContent
            likes=parseInt(l)
            likes++
            $('#like'+pitch)[0].textContent=' '+likes.toString()+' '
          }
        }
      }
    )
  }
  dislike=(pitch)=>{
    $.ajax(
      {
        url:'/dislike/'+pitch,
        method:'GET',
        success:(data)=>{
          if (data=='Success'){
            l=$('#dislike'+pitch)[0].textContent
            dislikes=parseInt(l)
            dislikes++
            $('#dislike'+pitch)[0].textContent=' '+dislikes.toString()+' '
          }
        }
      }
    )
  }
})
