# To use this test, call: shellspec spec/resource-count-aws.spec

Describe 'resource-count-aws'

  ########################################################################################
  # https://github.com/shellspec/shellspec#include---include-a-script-file
  ########################################################################################

  Include aws/resource-count-aws.sh

  ########################################################################################
  # https://github.com/shellspec/shellspec#function-based-mock
  ########################################################################################

  aws_ec2_describe_regions() {
    cat << EOJ
{
    "Regions": [
        {
            "Endpoint": "ec2.us-east-1.amazonaws.com",
            "RegionName": "us-east-1",
            "OptInStatus": "opt-in-not-required"
        },
        {
            "Endpoint": "ec2.us-east-2.amazonaws.com",
            "RegionName": "us-east-2",
            "OptInStatus": "opt-in-not-required"
        },
        {
            "Endpoint": "ec2.us-west-1.amazonaws.com",
            "RegionName": "us-west-1",
            "OptInStatus": "opt-in-not-required"
        },
        {
            "Endpoint": "ec2.us-west-2.amazonaws.com",
            "RegionName": "us-west-2",
            "OptInStatus": "opt-in-not-required"
        }
    ]
}
EOJ
  }

  aws_organizations_describe_organization() {
    cat << EOJ
{
    "Organization": {
        "MasterAccountArn": "arn:aws:organizations::011111111111:account/o-exampleorgid/011111111111",
        "MasterAccountEmail": "bill@example.com",
        "MasterAccountId": "011111111111",
        "Id": "o-exampleorgid",
        "FeatureSet": "ALL",
        "Arn": "arn:aws:organizations::011111111111:organization/o-exampleorgid",
        "AvailablePolicyTypes": [{
            "Status": "ENABLED",
            "Type": "SERVICE_CONTROL_POLICY"
        }]
    }
}
EOJ
  }

  aws_organizations_list_accounts() {
    cat << EOJ
{
    "Accounts": [{
            "Arn": "arn:aws:organizations::011111111111:account/o-exampleorgid/011111111111",
            "JoinedMethod": "INVITED",
            "JoinedTimestamp": 1481830215.45,
            "Id": "011111111111",
            "Name": "MasterAccount",
            "Email": "bill@example.com",
            "Status": "ACTIVE"
        },
        {
            "Arn": "arn:aws:organizations::011111111111:account/o-exampleorgid/222222222222",
            "JoinedMethod": "INVITED",
            "JoinedTimestamp": 1481835741.044,
            "Id": "222222222222",
            "Name": "ProductionAccount",
            "Email": "alice@example.com",
            "Status": "ACTIVE"
        },
        {
            "Arn": "arn:aws:organizations::011111111111:account/o-exampleorgid/333333333333",
            "JoinedMethod": "INVITED",
            "JoinedTimestamp": 1481835795.536,
            "Id": "333333333333",
            "Name": "DevelopmentAccount",
            "Email": "juan@example.com",
            "Status": "ACTIVE"
        },
        {
            "Arn": "arn:aws:organizations::011111111111:account/o-exampleorgid/444444444444",
            "JoinedMethod": "INVITED",
            "JoinedTimestamp": 1481835812.143,
            "Id": "444444444444",
            "Name": "TestAccount",
            "Email": "anika@example.com",
            "Status": "ACTIVE"
        }
    ]
}
EOJ
  }

  aws_sts_assume_role() {
    cat << EOJ
{
    "AssumedRoleUser": {
        "AssumedRoleId": "AROA3XFRBF535PLBIFPI4:s3-access-example",
        "Arn": "arn:aws:organizations::011111111111:account/o-exampleorgid/222222222222"
    },
    "Credentials": {
        "SecretAccessKey": "9drTJvcXLB89EXAMPLELB8923FB892xMFI",
        "SessionToken": "AQoXdzELDDY//////////wEaoAK1wvxJY12r2IrDFT2IvAzTCn3zHoZ7YNtpiQLF0MqZye/qwjzP2iEXAMPLEbw/m3hsj8VBTkPORGvr9jM5sgP+w9IZWZnU+LWhmg+a5fDi2oTGUYcdg9uexQ4mtCHIHfi4citgqZTgco40Yqr4lIlo4V2b2Dyauk0eYFNebHtYlFVgAUj+7Indz3LU0aTWk1WKIjHmmMCIoTkyYp/k7kUG7moeEYKSitwQIi6Gjn+nyzM+PtoA3685ixzv0R7i5rjQi0YE0lf1oeie3bDiNHncmzosRM6SFiPzSvp6h/32xQuZsjcypmwsPSDtTPYcs0+YN/8BRi2/IcrxSpnWEXAMPLEXSDFTAQAM6Dl9zR0tXoybnlrZIwMLlMi1Kcgo5OytwU=",
        "Expiration": "2020-12-15T00:00:00Z",
        "AccessKeyId": "EXAMPLE2222222EXAMPLE"
    }
}
EOJ
  }
 
  ####

  aws_ec2_describe_instances() {
    cat << EOJ
{
    "Reservations": [{
            "Groups": [],
            "Instances": [{
                    "InstanceId": "0abcdef1234567890"
                },
                {
                    "InstanceId": "0abcdef1234567891"
                }
            ]
        },
        {
            "Groups": [],
            "Instances": [{
                "InstanceId": "1abcdef1234567890"
            }]
        }
    ]
}
EOJ
  }

  aws_ec2_describe_db_instances() {
    cat << EOJ
{
    "Instances": [{
        "InstanceId": "0abcdef1234567890"
    }]
}
EOJ
  }

  aws_ec2_describe_nat_gateways() {
    cat << EOJ
{
    "Instances": [{
        "InstanceId": "0abcdef1234567890"
    }]
}
EOJ
  }

  aws_redshift_describe_clusters() {
    cat << EOJ
{
    "Instances": [{
        "InstanceId": "0abcdef1234567890"
    }]
}
EOJ
  }

  aws_elb_describe_load_balancers() {
    cat << EOJ
{
    "Instances": [{
        "InstanceId": "0abcdef1234567890"
    }]
}
EOJ
  }

aws_eks_list_clusters() {
  cat << EOJ
  {
    "clusters": [
        "eks-cluster-1"
    ]
  }
EOJ
}

aws_eks_list_nodegroups() {
  cat << EOJ
  {
    "nodegroups": [
        "nodes"
    ]
  }
EOJ
}

aws_eks_describe_nodegroup() {
  cat << EOJ
  {
    "nodegroup": {
      "scalingConfig": {
          "minSize": 2,
          "maxSize": 4,
          "desiredSize": 2
      }
    }
  }
EOJ
}

  aws_ecs_list_clusters() {
    cat << EOJ
{
    "clusterArns": [
        "arn:aws:ecs:us-west-2:123456789012:cluster/Cluster1",
        "arn:aws:ecs:us-west-2:123456789012:cluster/Cluster2"
    ]
}
EOJ
  }

  aws_ecs_list_tasks() {
    cat << EOJ
{
    "taskArns": [
        "arn:aws:ecs:us-west-2:123456789012:task/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
        "arn:aws:ecs:us-west-2:123456789012:task/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
        "arn:aws:ecs:us-west-2:123456789012:task/a1b2c3d4-5678-90ab-cdef-33333EXAMPLE"
    ]
}
EOJ
  }

  aws_lambda_get_account_settings() {
    cat << EOJ
{
    "AccountLimit": {},
    "AccountUsage": {
       "FunctionCount": 3
    }
}
EOJ
  }

  aws_s3api_list_buckets() {
    cat << EOJ
    [
      "testing123",
      "fakebucket456",
      "notyours789"
    ]
EOJ
  }

  aws_s3_ls_bucket_size() {
    echo "423451539000"
  }  

  ########################################################################################
  # https://github.com/shellspec/shellspec#it-specify-example---example-block
  ########################################################################################

  It 'returns a list of regions or the default list'
    When call get_region_list
    The output should not include "Warning:"
    The variable REGION_LIST[@] should eq "us-east-1 us-east-2 us-west-1 us-west-2"
  End

  ####

  It 'returns a list of one account'
    USE_AWS_ORG="false"
    When call get_account_list
    The output should not include "Error:"
    The variable TOTAL_ACCOUNTS should eq 1
  End

  It 'returns a list of organization member accounts'
    USE_AWS_ORG="true"
    #
    When call get_account_list
    The output should not include "Error:"
    The variable TOTAL_ACCOUNTS should eq 4
  End

  It 'assumes a role'
    MASTER_ACCOUNT_ID=011111111111
    #
    When call assume_role "ProductionAccount" 222222222222
    The output should not include "skipping"
    The variable AWS_ACCESS_KEY_ID should eq "EXAMPLE2222222EXAMPLE"
  End

  ####

  It 'returns a list of Regions'
    When call aws_ec2_describe_regions
    The output should not include "Error"
  End

  It 'returns a list of EC2 Instances'
    When call aws_ec2_describe_instances
    The output should not include "Error"
  End

  It 'returns a list of EKS Clusters'
    When call aws_eks_list_clusters
    The output should not include "Error"
  End

  It 'returns a list of nodegroups'
    When call aws_eks_list_nodegroups
    The output should not include "Error"
  End

  It 'returns details of a node group'
    When call aws_eks_describe_nodegroup
    The output should not include "Error"
  End

  It 'returns a list of ECS Clusters'
    When call aws_ecs_list_clusters
    The output should not include "Error"
  End

  It 'returns a list of ECS Tasks'
    When call aws_ecs_list_tasks
    The output should not include "Error"
  End

  It 'returns a list of RDS Instances'
    When call aws_ec2_describe_db_instances
    The output should not include "Error"
  End

  It 'returns a list of NAT Gateways'
    When call aws_ec2_describe_nat_gateways
    The output should not include "Error"
  End

  It 'returns a list of RedShift Clusters'
    When call aws_redshift_describe_clusters
    The output should not include "Error"
  End

  It 'returns a list of ELBs'
    When call aws_elb_describe_load_balancers
    The output should not include "Error"
  End

  It 'returns lambda function statistics'
    When call aws_lambda_get_account_settings
    The output should not include "Error"
  End

  It 'returns a list of S3 buckets'
    When call aws_s3api_list_buckets
    The output should not include "Error"
  End

  It 'returns the size of a single bucket'
    When call aws_s3_ls_bucket_size
    The output should not include "-1"
  End

  ########################################################################################
  # Note that resource totals are the result of the other mock api calls being called four times,
  # as a result of the mock api region call returning four regions. 
  ########################################################################################

  It 'counts account resources'
    USE_AWS_ORG="false"
    get_account_list > /dev/null 2>&1
    get_region_list  > /dev/null 2>&1
    reset_account_counters
    reset_global_counters
    #
    When call count_account_resources
    The output should include "Count"
    The variable TOTAL_ACCOUNTS should eq 1
    The variable WORKLOAD_COUNT_GLOBAL should eq 28
    The variable WORKLOAD_COUNT_GLOBAL_WITH_IAM_MODULE should eq 35
  End

  It 'counts organization member account resources'
    USE_AWS_ORG="true"
    get_account_list > /dev/null 2>&1
    get_region_list  > /dev/null 2>&1
    reset_account_counters
    reset_global_counters
    #
    When call count_account_resources
    The output should include "Count"
    The variable TOTAL_ACCOUNTS should eq 4
    The variable WORKLOAD_COUNT_GLOBAL should eq 112
    The variable WORKLOAD_COUNT_GLOBAL_WITH_IAM_MODULE should eq 140
  End

  It 'counts compute resources'
    USE_AWS_ORG="false"
    WITH_CWP="true"
    get_account_list > /dev/null 2>&1
    get_region_list  > /dev/null 2>&1
    reset_account_counters
    reset_global_counters
    #
    When call count_account_resources
    The output should include "Count"
    The variable LAMBDA_COUNT_GLOBAL should eq 12
    The variable LAMBDA_CREDIT_USAGE_GLOBAL should eq 2
    The variable EKS_CLUSTER_NODE_COUNT should eq 16
  End

  It 'counts data size'
    USE_AWS_ORG="false"
    WITH_DATA="true"
    get_account_list > /dev/null 2>&1
    get_region_list  > /dev/null 2>&1
    reset_account_counters
    reset_global_counters
    #
    When call count_account_resources
    The output should include "Count"
    The variable S3_BUCKETS_SIZE_GIG_GLOBAL should eq 1270
    The variable S3_BUCKETS_CREDIT_EXPOSURE_USAGE_GLOBAL should eq 6
    The variable S3_BUCKETS_CREDIT_FULL_USAGE_GLOBAL should eq 38
  End

End
