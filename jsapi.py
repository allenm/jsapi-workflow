#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 allenm <allenm@allenmMac.local>
#

import alp
import sqlite3

conn = sqlite3.connect('jsapi.db')
c = conn.cursor()

def uniMatch( matchs ):
  seen = set()
  seenAdd = seen.add
  return [ x for x in matchs if x[0] not in seen and not seenAdd( x[0] ) ]

def query( keyword ):

  #test = alp.Item(title="Array", subtitle="Array is", uid="a", valid=True , autocomplete="Array", arg="http://blog.allenm.me")

  #alp.feedback( test )

  keyword = '%'+keyword.strip()+'%'


  c.execute('''SELECT OID,* FROM jsapi WHERE name LIKE ? LIMIT 10''', ( keyword, ))

  nameMatch = c.fetchall()


  c.execute('''SELECT OID,* FROM jsapi WHERE t2 LIKE ? LIMIT 10''', ( keyword, ))

  t2Match = c.fetchall()

  allMatch = nameMatch + t2Match
 
  allMatch = uniMatch( allMatch )[0:10]


  items = []
  for index ,match in enumerate(allMatch):
    title = match[3] + ' ('+ match[2] +')'
    item = alp.Item( title= title , subtitle = match[4], uid= str(index ), valid=True, autocomplete = match[3], arg= match[5] )
    items.append( item )

  alp.feedback( items )


if __name__ == "__main__":
  query('slice')

