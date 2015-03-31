echo off

cls

echo Bienvenido a Freeling!

set /p text1 = Ingrese texto del documento 1:

echo %text1% >  C:\Users\JP\Desktop\TT\PLN\programa_vsm\prueba_doc1.txt

pause

echo analyzer -f "%FREELINGSHARE%\config\es.cfg" < C:\Users\JP\Desktop\TT\PLN\programa_vsm\prueba_doc1.txt > C:\Users\JP\Desktop\TT\PLN\programa_vsm\res_prueba_doc1.txt

pause

set /p text2 = Ingrese texto del documento 2:


%text2% >  C:\Users\JP\Desktop\TT\PLN\programa_vsm\prueba_doc2.txt

pause

echo analyzer -f "%FREELINGSHARE%\config\es.cfg" < C:\Users\JP\Desktop\TT\PLN\programa_vsm\prueba_doc2.txt > C:\Users\JP\Desktop\TT\PLN\programa_vsm\res_prueba_doc2.txt

pause

set /p consulta =  Ingrese la consulta:
echo %consulta% >  C:\Users\JP\Desktop\TT\PLN\programa_vsm\prueba_consulta.txt

echo analyzer -f "%FREELINGSHARE%\config\es.cfg" < C:\Users\JP\Desktop\TT\PLN\programa_vsm\prueba_consulta.txt > C:\Users\JP\Desktop\TT\PLN\programa_vsm\res_prueba_consulta.txt
pause