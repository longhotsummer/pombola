# Mzalendo

This web app allows you to store and share information on public figures,
especially politicians.

Please see the [Operations Manual](http://goo.gl/uaXup) which covers all aspects of running a Mzalendo site.

For an overview of the system please see the files in docs/ - especially
[OVERVIEW.txt](https://github.com/mysociety/mzalendo/blob/master/docs/OVERVIEW.txt)


## Community

Please join the Mzalendo Users Google group for discussion about running Mzalendo-based websites. This is also where announcements etc will be made.

    https://groups.google.com/forum/?fromgroups=#!forum/mzalendo-users

There is also the Components mailing list for some of the code used to make the site. This includes [MapIt](https://github.com/mysociety/mapit) (for the boundaries) and [PopIt](https://github.com/mysociety/popit) (a data storage engine that Mzalendo will be changed to use in the future):

    https://secure.mysociety.org/admin/lists/mailman/listinfo/components


## Installing

Please see [docs/INSTALL.txt](https://github.com/mysociety/mzalendo/blob/master/docs/INSTALL.txt)


## Troubleshooting

Please see [docs/TROUBLESHOOTING.txt](https://github.com/mysociety/mzalendo/blob/master/docs/TROUBLESHOOTING.txt) file

## Future

The Mzalendo codebase was originally written for the Kenyan site [mzalendo.com](http://info.mzalendo.com). It has since been modified to support other sites - notably one in Nigeria.

We want the code to be easy to use for other installations, but currently there are some rough edges.

We also intend to replace the `core` app's models with an external data store. This will be done using [PopIt](https://github.com/mysociety/popit) which is a project that we are currently working on.
