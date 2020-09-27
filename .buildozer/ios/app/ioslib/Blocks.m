#import "Blocks.h"

@implementation StepWorker

- (id) init {
    if(self = [super init]) {
        self.pedometer = [[CMPedometer alloc] init];
        queue = [[NSOperationQueue alloc] init];
    }
    return self;
}

- (void)startPedometer {
    printf("hello");

    if ([CMPedometer isStepCountingAvailable]) {

      [self.pedometer startPedometerUpdatesFromDate:[NSDate date]
                                      withHandler:^(CMPedometerData *pedometerData, NSError *error) {
                                          dispatch_async(dispatch_get_main_queue(), ^{
                                              self.stepNumber = [pedometerData.numberOfSteps doubleValue];
                                              self.distance = [pedometerData.distance doubleValue];
                                          });
                                      }];
    }
}

- (void)stopPedometer {
    printf("goodbye");
    [self.pedometer stopPedometerUpdates];
}

- (void) dealloc {
    [self.pedometer release];
    [queue release];
    [super dealloc];
}

@end
