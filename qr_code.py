# Simple qrcode generator
import qrcode as qr
img = qr.make("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=12368567762611962800&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062039&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")
img.save("Amazon_india.png")
