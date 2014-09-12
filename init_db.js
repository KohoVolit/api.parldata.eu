/* A script to initialize database for a new parliament.
 *
 * Use in mongo shell by:
 *
 *     > use <db-name>
 *     > load("<absolute-path>/init_db.js")
 */

// create indexes on People
db.people.ensureIndex({"name": 1});
db.people.ensureIndex({"identifiers.identifier": 1});
db.people.ensureIndex({"family_name": 1});
db.people.ensureIndex({"sort_name": 1});

// create indexes on Organizations
db.organizations.ensureIndex({"name": 1});
db.organizations.ensureIndex({"identifiers.identifier": 1});
db.organizations.ensureIndex({"classification": 1});
db.organizations.ensureIndex({"parent_id": 1});

// create indexes on Memberships
db.memberships.ensureIndex({"person_id": 1});
db.memberships.ensureIndex({"organization_id": 1});
db.memberships.ensureIndex({"on_behalf_of_id": 1}, {sparse: true});
db.memberships.ensureIndex({"post_id": 1}, {sparse: true});

// create indexes on Posts
db.posts.ensureIndex({"label": 1});
db.posts.ensureIndex({"organization_id": 1});

// create indexes on Areas
db.areas.ensureIndex({"name": 1});
db.areas.ensureIndex({"identifier": 1});
db.areas.ensureIndex({"classification": 1});
db.areas.ensureIndex({"parent_id": 1});

// create indexes on Motions
db.motions.ensureIndex({"organization_id": 1});
db.motions.ensureIndex({"creator_id": 1});
db.motions.ensureIndex({"text": "hashed"});	// hashed because of 1024B key size limit
db.motions.ensureIndex({"date": 1});

// create indexes on Vote events
db.vote_events.ensureIndex({"identifier": 1});
db.vote_events.ensureIndex({"motion_id": 1});
db.vote_events.ensureIndex({"start_date": 1});
db.vote_events.ensureIndex({"end_date": 1});

// create indexes on Votes
db.votes.ensureIndex({"vote_event_id": 1});
db.votes.ensureIndex({"voter_id": 1}, {sparse: true});
db.votes.ensureIndex({"group_id": 1}, {sparse: true});
db.votes.ensureIndex({"pair_id": 1}, {sparse: true});

// create indexes on Logs
db.logs.ensureIndex({"created_at": 1});
