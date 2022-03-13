def strip_between( s, first,last):
    try:
        start = s.index( first ) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return s

str = '''<td>id=logInPanelHeading<datalist><option>id=logInPanelHeading</option><option>xpath=(.//*[normalize-space(text()) and normalize-space(.)=concat('Nom d', "'", 'utilisateur')])[1]/preceding::div[1]</option><option>xpath=(.//*[normalize-space(text()) and normalize-space(.)='Mot de passe'])[1]/preceding::div[2]</option><option>//div[@id='logInPanelHeading']</option><option>//form[@id='frmLogin']/div</option><option>//form/div</option><option>css=#logInPanelHeading</option></datalist></td>'''

str1 = "Open the file moby_dick.txt as read-only and"
# print(strip_until(str,'exemple','base'))
# subs = strip_between(str1, "file", "as")
# subs = strip_between(str1, "file", "as")
subs = find_between_r(str, "<datalist>", "</datalist>")

print(subs)

