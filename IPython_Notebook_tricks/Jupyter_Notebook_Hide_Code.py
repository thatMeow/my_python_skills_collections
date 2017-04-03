from IPython.display import HTML # Use this module to hide Python scripts and only show results

# This piece of code enable us to view/ hide Python code. For presentations we don't need to see the code

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to show/ hide the Python code"></form>''')
