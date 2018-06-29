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
          ('#pitches').html(data)
        },
        error: (data)=>{
          alert('Could not post pitch')
        }
      }
    )
  })
})
