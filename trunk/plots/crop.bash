for i in *.pdf
do
  oname=`basename $i .pdf`-old.pdf
  mv $i $oname
  pdfcrop --margins 0 $oname $i
done