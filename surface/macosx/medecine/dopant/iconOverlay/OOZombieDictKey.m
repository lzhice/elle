//
//  OOZombieDictKey.m
//  Dopant
//
//  Created by Charles Guillot on 02/04/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import "OOZombieDictKey.h"

@implementation OOZombieDictKey

@synthesize linkedDictKeys;
@synthesize parent;

- (id) init
{
    self = [super init];
    
    if (!self.linkedDictKeys) {
        self.linkedDictKeys = [[NSMutableArray alloc] init];
    }
    
    return self;
}

- (void) addDictKey:(id)arg1
{
    [self.linkedDictKeys addObject:arg1];
}

- (void) dealloc
{
    for (id<OOCellDictKey_Protocol> dictKey in self.linkedDictKeys) {
        [dictKey cleanUp];
    }
    [self.linkedDictKeys removeAllObjects];
    [linkedDictKeys release];
    [super dealloc];
}

@end
