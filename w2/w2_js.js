function calculate(min,max,step){
    let sum = 0;
    for(let i=min; i<=max; i+=step){
      sum += i;
    };
    console.log(sum);
  }
  
  calculate(1,3,1);
  calculate(4,8,2);
  calculate(-1,2,2);
  
  function avg(data){
    let count = 0;
    let sum = 0;
    for(let i=0;i<data.employees.length;i++){
      if(!(data.employees[i].manager)){
        sum = sum + data.employees[i].salary;
        count++; 
      };
    };
    console.log(sum/count);
  }
  
  avg({
      "employees":[ 
          {   
              "name":"John", 
              "salary":30000, 
              "manager":false
          }, 
          {
              "name":"Bob", 
              "salary":60000, 
              "manager":true
          }, 
          {
              "name":"Jenny", 
              "salary":50000, 
              "manager":false
          }, 
          {
              "name":"Tony", 
              "salary":40000, 
              "manager":false
          }
      ]
  });
  
  function func(a){
    function sum(b,c){
      console.log(a+b*c);
      return;
    };
    return sum;
  };
  
  func(2)(3,4);
  func(5)(1,-5)
  func(-3)(2,9)
  
  function maxProduct(nums){
    let max = 0;
    if (nums.length == 2){
      console.log(nums[0]*nums[1]);
      return;
    }
    for(let i=0;i<(nums.length-1);i++){
      for(let j=i+1;j<nums.length;j++){
        if (nums[i]*nums[j]<0){
          continue;
        }else{
          max_temp = nums[i]*nums[j];
          if(max_temp > max){
            max = max_temp;
          };
        };
      };
    };
    console.log(max);
  };
  
  maxProduct([5,20,2,6])    //120
  maxProduct([10,-20,0,3])  //30
  maxProduct([10,-20,0,-3]) //60
  maxProduct([-1,2])        //-2
  maxProduct([-1,0,2])      //0
  maxProduct([5,-1,-2,0])   //2
  maxProduct([-5,-2])       //10
  
  
  function twoSum(nums,target){
    for(let i=0;i<(nums.length-1);i++){
      for(let j=i+1;j<nums.length;j++){
        if(nums[i]+nums[j] == target){
          return [i,j];
        };
      };
    };
  };
  let result = twoSum([2,11,7,15],9);
  console.log(result);
  
  function maxZeros(nums){
    let count = 0;
    let max_count = 0;
    for(let i=0;i<nums.length;i++){
      if(nums[i]==0){
        count += 1;
      }else{
        if (count>max_count){
          max_count = count;
          count = 0;
        };
      };
    };
    if (count>max_count){
      max_count = count;
    };
    console.log(max_count);
  };
  
  maxZeros([0,1,0,0]);
  maxZeros([1,0,0,0,0,1,0,1,0,0]);
  maxZeros([1,1,1,1]);
  maxZeros([0,0,0,1,1]);
  
  
  
  
  