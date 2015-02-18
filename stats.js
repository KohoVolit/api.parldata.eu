/* Print statistics about contents of databases.
 *
 * Use in TokuMX shell by:
 *
 *     > use <db-name>
 *     > load("<absolute-path>/init_db.js")
 */

countValues = function(d, collection, fields) {
	totals = d[collection].aggregate([
		{$group: {_id: fields, total: {$sum: 1}}}]);

	info = '';
	totals.result.forEach(function(sum){
		for(key in sum._id)
			info = info + sum._id[key] + '.';
		info = info + "=" + sum.total + ", ";
	});
	print('\t' + info);
}

db.adminCommand('listDatabases').databases.forEach(function(dbinfo) {
	name = dbinfo.name;
	if (name.indexOf('_') == -1)
		return;

	print('');
	print(" ---- " + name + " ----");
	
	d = db.getSiblingDB(name);
	d.getCollectionNames().forEach(function(name) {
		if (name == 'system.indexes')
			return;

		count = d[name].count();
		sources_count = d[name].find({'sources': {$elemMatch: {'url': {$exists: true}}}}).count()
		print(name + ": " + count + " rows, source set in " + sources_count);

		if (count > 0) {
		if (name == 'organizations') {
			countValues(d, name, {classification: '$classification'});
		}
		if (name == 'logs')
			countValues(d, name, {status: '$status'});
		}
	});
});

