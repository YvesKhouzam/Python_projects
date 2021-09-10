import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('yveskhouzam@gmail.com', 'snsctwalgdxmtctv')
conn.sendmail('yveskhouzam@gmail.com', 'yveskhouzam@hotmail.com', 'Subject: Yo...\n\n Dear Yves mange la patate.\n\n-Gille')
{}
quit()