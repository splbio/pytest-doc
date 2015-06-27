import json

def tattr_init(f):
    if not hasattr(f, 'tattr'):
        f.tattr = {}

def tattr_category(category):
    def wrap(f):
        tattr_init(f)
        f.tattr['category'] = category
        return f
    return wrap

def tattr_doc(doc):
    def wrap(f):
        tattr_init(f)
        f.tattr['docstr'] = doc
        return f
    return wrap

def tattr_annotate_bug(f, bugids, tracker, bugtype):
    tattr_init(f)
    bugs = []
    assert(bugtype in ['feature', 'bug'])
    assert(tracker in ['redmine', 'gitlab'])
    for bugid in bugids:
        #print "Appending %s -> %s" % (bugid, bugtype)
        bugs.append({
            'id': bugid,
            'tracker': tracker,
            'bugtype': bugtype,
        })
    if not 'bugs' in f.tattr:
        f.tattr['bugs'] = []
    f.tattr['bugs'].extend(bugs)
    #print json.dumps(f.tattr, indent=4)

def tattr_redmine_feature(*bugids):
    def wrap(f):
        tattr_annotate_bug(f, bugids, 'redmine', 'feature')
        return f
    return wrap

def tattr_redmine_bug(*bugids):
    def wrap(f):
        tattr_annotate_bug(f, bugids, 'redmine', 'bug')
        return f
    return wrap

def tattr_incomplete(f):
    tattr_init(f)
    f.tattr['incomplete'] = True
    return f
