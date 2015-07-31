my_data = [
    {'event_date': '18-06-2015', 'fatalities': 9.0},
    {'event_date': '16-07-2015', 'fatalities': 5.0},
    {'event_date': '23-05-2014', 'fatalities': 7.0},
    {'event_date': '20-02-2014', 'fatalities': 4.0},
    {'event_date': '24-10-2014', 'fatalities': 5.0},
    {'event_date': '07-06-2013', 'fatalities': 6.0},
    {'event_date': '16-09-2013', 'fatalities': 13.0},
    {'event_date': '07-26-2013', 'fatalities': 6.0},
    {'event_date': '21-04-2013', 'fatalities': 5.0},
    {'event_date': '13-03-2013', 'fatalities': 5.0},
    {'event_date': '20-07-2012', 'fatalities': 12.0},
    {'event_date': '05-08-2012', 'fatalities': 7.0},
    {'event_date': '27-09-2012', 'fatalities': 7.0},
    {'event_date': '14-12-2012', 'fatalities': 27.0},
    {'event_date': '02-04-2012', 'fatalities': 7.0},
    {'event_date': '22-02-2012', 'fatalities': 5.0},
    {'event_date': '20-05-2012', 'fatalities': 6.0},
    {'event_date': '16-04-2007', 'fatalities': 33.0},
    {'event_date': '16-10-1991', 'fatalities': 24.0},
    {'event_date': '18-07-1984', 'fatalities': 21.0},
    {'event_date': '01-08-1966', 'fatalities': 18.0},
    {'event_date': '20-08-1986', 'fatalities': 15.0},
    {'event_date': '05-11-2009', 'fatalities': 13.0},
    {'event_date': '03-04-2009', 'fatalities': 13.0},
    {'event_date': '20-04-1999', 'fatalities': 13.0},
    {'event_date': '18-02-1983', 'fatalities': 13.0},
    {'event_date': '05-09-1949', 'fatalities': 13.0},
    {'event_date': '29-07-1999', 'fatalities': 12.0},
    {'event_date': '10-03-2009', 'fatalities': 10.0},
    {'event_date': '21-03-2005', 'fatalities': 10.0},
    {'event_date': '18-06-1990', 'fatalities': 10.0},
    {'event_date': '14-10-2011', 'fatalities': 8.0},
    {'event_date': '03-08-2010', 'fatalities': 9.0},
    {'event_date': '19-01-2010', 'fatalities': 8.0},
    {'event_date': '29-03-2009', 'fatalities': 8.0},
    {'event_date': '05-12-2007', 'fatalities': 8.0},
    {'event_date': '01-07-1993', 'fatalities': 8.0},
    {'event_date': '14-09-1989', 'fatalities': 8.0},
    {'event_date': '20-08-1982', 'fatalities': 8.0},
    {'event_date': '17-01-1989', 'fatalities': 5.0},
    {'event_date': '11-01-1991', 'fatalities': 6.0},
    {'event_date': '01-05-1992', 'fatalities': 4.0},
    {'event_date': '07-12-1993', 'fatalities': 6.0},
    {'event_date': '24-03-1998', 'fatalities': 5.0},
    {'event_date': '29-07-1999', 'fatalities': 9.0},
    {'event_date': '15-09-1999', 'fatalities': 7.0},
    {'event_date': '02-11-1999', 'fatalities': 7.0},
    {'event_date': '26-12-2000', 'fatalities': 7.0},
    {'event_date': '08-07-2003', 'fatalities': 7.0},
    {'event_date': '02-10-2006', 'fatalities': 5.0},
    {'event_date': '25-03-2006', 'fatalities': 7.0},
    {'event_date': '30-01-2006', 'fatalities': 8.0},
    {'event_date': '12-02-2007', 'fatalities': 5.0},
    {'event_date': '14-02-2008', 'fatalities': 6.0},
    {'event_date': '06-09-2011', 'fatalities': 5.0},
    {'event_date': '08-01-2011', 'fatalities': 6.0},
    {'event_date': '29-06-1984', 'fatalities': 6.0},
    {'event_date': '23-04-1987', 'fatalities': 7.0},
    {'event_date': '16-02-1988', 'fatalities': 7.0},
    {'event_date': '14-11-1991', 'fatalities': 5.0},
    {'event_date': '15-10-1992', 'fatalities': 5.0},
    {'event_date': '06-08-1993', 'fatalities': 4.0},
    {'event_date': '14-12-1993', 'fatalities': 4.0},
    {'event_date': '20-06-1994', 'fatalities': 5.0},
    {'event_date': '03-04-1995', 'fatalities': 6.0},
    {'event_date': '09-02-1996', 'fatalities': 6.0},
    {'event_date': '15-09-1997', 'fatalities': 4.0},
    {'event_date': '18-02-1997', 'fatalities': 5.0},
    {'event_date': '21-05-1998', 'fatalities': 4.0},
    {'event_date': '06-03-1998', 'fatalities': 5.0},
    {'event_date': '05-02-2001', 'fatalities': 5.0},
    {'event_date': '08-12-2004', 'fatalities': 5.0},
    {'event_date': '03-12-2005', 'fatalities': 7.0},
    {'event_date': '07-10-2007', 'fatalities': 6.0},
    {'event_date': '25-06-2008', 'fatalities': 6.0},
    {'event_date': '07-02-2008', 'fatalities': 6.0},
    {'event_date': '02-04-2009', 'fatalities': 7.0}
]

data_by_frequency = []

for d in my_data:
    for x in xrange(0, int(d['fatalities'])):
        #print {'event_date': d['event_date'], 'fatalities': float(x+1), 'total': d['fatalities']}

        print "{'event_date': '" + str(d['event_date']) + "', 'fatalities': " + str(float(x+1)) + ", 'total': " + str(d['fatalities']) + "},"



        # data_by_frequency.append(
        #     {'event_date': d['event_date'], 'total': d['fatalities'], 'fatalities': float(x+1)}
        # )


#print data_by_frequency