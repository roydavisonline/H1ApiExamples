USE [HackerOneData]
GO

/****** Object:  StoredProcedure [dbo].[UpsertData]    Script Date: 10/6/2022 12:55:47 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		Roy Davis
-- Create date: 11-2-2021
-- Description:	Insert or update a data record
-- =============================================
CREATE PROCEDURE [dbo].[UpsertHackerOneData] 	
	@reportId nvarchar(50),
	@bbProgramId nvarchar(50),
	@reportState nvarchar(50),
	@reportCreatedDateTime datetime,
	@reportVulnerabilityInformation varchar(MAX),
	@reportTitle nvarchar(150),
	@reportTriagedDateTime datetime,
	@reportClosedDateTime datetime,
	@reportLastReporterActivityDateTime datetime,
	@reportFirstProgramActivityDateTime datetime,
	@reportLastProgramActivityDateTime datetime,
	@reportBountyAwardedDateTime datetime,
	@reportBountyAwardedAmount money,
	@reportSwagAwardedDateTime datetime,
	@reportDisclosedDateTime datetime,
	@reportLastPublicActivityDateTime datetime,
	@reportLastActivityDateTime datetime,
	@reportIssueTrackerUrl nvarchar(150),
	@researcherUsername nvarchar(512),
	@researcherName nvarchar(512),
	@researcherReputation nvarchar(10),
	@researcherSignal nvarchar(10),
	@researcherImpact nvarchar(10),
	@reportSeverityCVSSRating nvarchar(50),
	@reportSeverityCVSSScore nvarchar(10),
	@reportSeverityCVSSSComplexity nvarchar(10),
	@reportSeverityCVSSSVector nvarchar(10),
	@reportSeverityCVSSSAvailability nvarchar(10),
	@reportSeverityCVSSConfidentiality nvarchar(10),
	@reportSeverityCVSSIntegrity nvarchar(10),
	@reportSeverityCVSSPrivileges nvarchar(10),
	@reportSeverityCVSSUserInteraction nvarchar(10),
	@reportSeverityCVSSScopeChange nvarchar(10),
	@reportWeaknessName nvarchar(150),
	@reportWeaknessCWEID nvarchar(50),
	@reportScopeAssetType nvarchar(50),
	@reportScopeAssetIdentifier nvarchar(50),
	@reportCustomFieldSubTakeover nvarchar(50),
	@reportCustomFieldIPaddress nvarchar(50),
	@ipAddressCountry nvarchar(50),
	@ipAddressCountryCode nvarchar(50),
	@ipAddressCity nvarchar(50),
	@ipAddressRegion nvarchar(50),
	@ipAddressPostalCode nvarchar(50),
	@ipAddressLatitude nvarchar(50),
	@ipAddressLongitude nvarchar(50)
AS
BEGIN
	update HackerOneData.dbo.Reports
	set bbProgramId = @bbProgramId,
		reportState = @reportState,
		reportCreatedDateTime = @reportCreatedDateTime,
		reportVulnerabilityInformation = @reportVulnerabilityInformation,
		reportTitle = @reportTitle,
		reportTriagedDateTime = @reportTriagedDateTime,
		reportClosedDateTime = @reportClosedDateTime,
		reportLastReporterActivityDateTime = @reportLastReporterActivityDateTime,
		reportFirstProgramActivityDateTime = @reportFirstProgramActivityDateTime,
		reportLastProgramActivityDateTime = @reportLastProgramActivityDateTime,
		reportBountyAwardedDateTime = @reportBountyAwardedDateTime,
		reportBountyAwardedAmount = @reportBountyAwardedAmount,
		reportSwagAwardedDateTime = @reportSwagAwardedDateTime,
		reportDisclosedDateTime = @reportDisclosedDateTime,
		reportLastPublicActivityDateTime = @reportLastPublicActivityDateTime,
		reportLastActivityDateTime = @reportLastActivityDateTime,
		reportIssueTrackerUrl = @reportIssueTrackerUrl,
		researcherUsername = @researcherUsername,
		researcherName = @researcherName,
		researcherReputation = @researcherReputation,
		researcherSignal = @researcherSignal,
		researcherImpact = @researcherImpact,
		reportSeverityCVSSRating = @reportSeverityCVSSRating,
		reportSeverityCVSSScore = @reportSeverityCVSSScore,
		reportSeverityCVSSSComplexity = @reportSeverityCVSSSComplexity,
		reportSeverityCVSSSVector = @reportSeverityCVSSSVector,
		reportSeverityCVSSSAvailability = @reportSeverityCVSSSAvailability,
		reportSeverityCVSSConfidentiality = @reportSeverityCVSSConfidentiality,
		reportSeverityCVSSIntegrity = @reportSeverityCVSSIntegrity,
		reportSeverityCVSSPrivileges = @reportSeverityCVSSPrivileges,
		reportSeverityCVSSUserInteraction = @reportSeverityCVSSUserInteraction,
		reportSeverityCVSSScopeChange = @reportSeverityCVSSScopeChange,
		reportWeaknessName = @reportWeaknessName,
		reportWeaknessCWEID = @reportWeaknessCWEID,
		reportScopeAssetType = @reportScopeAssetType,
		reportScopeAssetIdentifier = @reportScopeAssetIdentifier,
		reportCustomFieldSubTakeover = @reportCustomFieldSubTakeover,
		reportCustomFieldIPaddress = @reportCustomFieldIPaddress
	where reportId = @reportId

	-- If no update took place, do the insert
	if @@ROWCOUNT = 0
		insert into HackerOneData.dbo.Reports(reportId,bbProgramId,reportState,reportCreatedDateTime,reportVulnerabilityInformation,reportTitle,reportTriagedDateTime,reportClosedDateTime,reportLastReporterActivityDateTime,reportFirstProgramActivityDateTime,reportLastProgramActivityDateTime,reportBountyAwardedDateTime,reportBountyAwardedAmount,reportSwagAwardedDateTime,reportDisclosedDateTime,reportLastPublicActivityDateTime,reportLastActivityDateTime,reportIssueTrackerUrl,researcherUsername,researcherName,researcherReputation,researcherSignal,researcherImpact,reportSeverityCVSSRating,reportSeverityCVSSScore,reportSeverityCVSSSComplexity,reportSeverityCVSSSVector,reportSeverityCVSSSAvailability,reportSeverityCVSSConfidentiality,reportSeverityCVSSIntegrity,reportSeverityCVSSPrivileges,reportSeverityCVSSUserInteraction,reportSeverityCVSSScopeChange,reportWeaknessName,reportWeaknessCWEID,reportScopeAssetType,reportScopeAssetIdentifier,reportCustomFieldSubTakeover)
		values (@reportId,@bbProgramId,@reportState,@reportCreatedDateTime,@reportVulnerabilityInformation,@reportTitle,@reportTriagedDateTime,@reportClosedDateTime,@reportLastReporterActivityDateTime,@reportFirstProgramActivityDateTime,@reportLastProgramActivityDateTime,@reportBountyAwardedDateTime,@reportBountyAwardedAmount,@reportSwagAwardedDateTime,@reportDisclosedDateTime,@reportLastPublicActivityDateTime,@reportLastActivityDateTime,@reportIssueTrackerUrl,@researcherUsername,@researcherName,@researcherReputation,@researcherSignal,@researcherImpact,@reportSeverityCVSSRating,@reportSeverityCVSSScore,@reportSeverityCVSSSComplexity,@reportSeverityCVSSSVector,@reportSeverityCVSSSAvailability,@reportSeverityCVSSConfidentiality,@reportSeverityCVSSIntegrity,@reportSeverityCVSSPrivileges,@reportSeverityCVSSUserInteraction,@reportSeverityCVSSScopeChange,@reportWeaknessName,@reportWeaknessCWEID,@reportScopeAssetType,@reportScopeAssetIdentifier,@reportCustomFieldSubTakeover)
END
GO


