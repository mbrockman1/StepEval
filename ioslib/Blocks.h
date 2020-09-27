#import <Foundation/Foundation.h>
#import <CoreMotion/CoreMotion.h>


@interface StepWorker : NSObject {
    NSOperationQueue *queue;
}

@property (strong, nonatomic) CMPedometer *pedometer;
@property (nonatomic) double stepNumber;
@property (nonatomic) double distance;

@end
