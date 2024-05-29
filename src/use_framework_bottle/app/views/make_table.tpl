<form action="/new">
    <input type="submit" value="New tO dO" />
</form>
<p>The list :</p>
<table border="1">
%if len(rows) > 0:
  <tr>
  %for col_name in ['ID', 'Task', 'Status']:
    <th>{{col_name}}</th>
  %end
  </tr>
%end
%for row in rows:
  <tr>
    <td>{{row[0]}}</td>
    <td><a href="/edit/{{row[0]}}">{{row[1]}}</a></td>
    <td>{{'1' if row[2] == 1 else '0'}}</td>
  </tr>
%end
</table>
