from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>hello world</h1>')
def mycode(request):
    return HttpResponse('<div style="color:red">first code</div><br>lalal<br>')
def zh(request,name,age):
    return HttpResponse('i am %s,%s years old'%(name,age))
def birthday(request,mon,day):
    import time
    T1=time.mktime((2019,int(mon),int(day),0,0,0,0,0,0))
    T2=time.localtime(T1)
    return HttpResponse('你的生日是今年的第%d天'%T2.tm_yday)
def chengfa(request):
    # for i in range(1,10):
    #     for j in range(1,i+1):
    #         print('%d * %d = %d'%(j,i,j*i),end='\t')
    #     print('\n')

    html="""
    <html>
    <head>
        <meta charset = "UTF-8" >
        <title></title >
    </head>
    <body>
        <script>
            var str = '<table>';
            for (var i=1;i <= 9;i++){
                str+='<tr>'
                for (var j=1;j <= i;j++){
                    str += '<td>'+j+'*'+i+'='+j * i+'</td>';
                    }
                str += '</tr>';
             }
            str += '</table>';
            document.write(str);
        </script>
    </body >
    </html >
"""
# str=''
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             str+='%d * %d = %d' % (j, i, j * i)+'\t'
#         str+='\n'
    return HttpResponse(html)